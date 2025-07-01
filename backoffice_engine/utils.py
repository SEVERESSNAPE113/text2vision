from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from backoffice_engine.models import Generated_image
from django.shortcuts import redirect
import traceback

def text2vision(user_prompt, creativity, user_object, category, instruction):
    try:
        client = genai.Client(api_key="AIzaSyDX-pSfut3_tHQEog99OKPY4AwKuNgI2GY")
        system_prompt = "i will pass your system generated text in an image model, so give me output as an image input prompt."
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    max_output_tokens=1000,
                    temperature=int(int(creativity) / 100)
                ),
            
                contents=user_prompt
            )
            print(response)
            contents = (response.text,)
        except Exception as e:
            traceback.print_exc()
            return redirect("/generate_image/")

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'] 
                )
            )
        except Exception as e:
            traceback.print_exc()
            return redirect("/generate_image/")

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                image_io = BytesIO()
                image.save(image_io, format='PNG')
                image_io.seek(0)

                generated_image = Generated_image.objects.create(
                    user=user_object,
                    system_prompt=category,
                    user_prompt=instruction,
                    temprature=int(creativity) / 100
                )
                image_file = ContentFile(image_io.read(), name=f"{generated_image.id}.png")
                generated_image.image = image_file
                generated_image.save()
                return generated_image

    except Exception as e:
        traceback.print_exc()
        return redirect("/generate_image/")
