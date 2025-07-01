from django.db.models.signals import post_migrate
from django.dispatch import receiver
from backoffice_engine.models import Plan, Suggested_prompt, Category


@receiver(post_migrate)
def create_default_plans(sender, **kwargs):
    if sender.name != 'backoffice_engine':
        return

    default_plans = [
        {"name": "FREE", "description": "", "price": 0, "duration_days": 30, "credit": 5},
        {"name": "PRO", "description": "", "price": 499, "duration_days": 30, "credit": 20},
        {"name": "PREMIUM", "description": "", "price": 999, "duration_days": 30, "credit": 75},
        {"name": "PRO[365]", "description": "", "price": 7500, "duration_days": 365, "credit": 500},
        {"name": "PREMIUM[365]", "description": "", "price": 10000, "duration_days": 365, "credit": 950},
    ]

    for plan in default_plans:
        obj, created = Plan.objects.get_or_create(
            name=plan["name"],
            defaults={
                "description": plan["description"],
                "price": plan["price"],
                "duration_days": plan["duration_days"],
                "credit": plan["credit"],
                "is_active": True
            }
        )
        if created:
            print(f"Created plan: {plan['name']}")
        else:
            print(f"Plan already exists: {plan['name']}")


@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name != 'backoffice_engine':
        return

    default_categories = [
        {"name": "Nature", "description": ""},
        {"name": "Architecture", "description": ""},
        {"name": "People / Characters", "description": ""},
        {"name": "Animals", "description": ""},
        {"name": "Art Styles", "description": ""},
        {"name": "Concepts / Abstract", "description": ""},
        {"name": "Products / Designs", "description": ""},
        {"name": "Special Themes", "description": ""},
        {"name": "Fantasy", "description": ""},
        {"name": "Sci-fi", "description": ""},
        {"name": "Horror", "description": ""},
        {"name": "Cartoon", "description": ""},
        {"name": "Logo", "description": ""},
        {"name": "Fashion", "description": ""},
        {"name": "Vehicles", "description": ""},
        {"name": "Food", "description": ""},
        {"name": "Sports", "description": ""},
        {"name": "Technology", "description": ""},
        {"name": "Mythology", "description": ""},
        {"name": "Emotions / Expressions", "description": ""},
        {"name": "Historical", "description": ""},
        {"name": "Space / Astronomy", "description": ""},
        {"name": "Minimalism", "description": ""},
        {"name": "Typography", "description": ""},
        {"name": "Glitch / Cyber", "description": ""},
        {"name": "Dreams / Surreal", "description": ""},
    ]

    for cat in default_categories:
        obj, created = Category.objects.get_or_create(
            name=cat["name"],
            defaults={"description": cat["description"]}
        )
        if created:
            print(f"Created category: {cat['name']}")
        else:
            print(f"Category already exists: {cat['name']}")


@receiver(post_migrate)
def create_default_suggested_prompts(sender, **kwargs):
    if sender.name != 'backoffice_engine':
        return

    default_prompts = [
        "A futuristic city at night",
        "A cute cat wearing sunglasses",
        "A magical forest with glowing plants",
        "A dragon flying over mountains",
        "A retro-futuristic robot design",
        "A mysterious castle in the clouds",
        "A cyberpunk street market with neon signs",
        "A peaceful village by a crystal-clear lake",
        "An astronaut standing on an alien planet",
        "A steampunk airship flying over a desert",
        "A giant whale swimming through the sky",
        "A magical library with floating books",
        "A warrior standing in a fiery battlefield",
        "A fairy sitting on a glowing mushroom",
        "A futuristic car speeding through a neon tunnel",
        "A dark forest with glowing eyes in the shadows",
        "A fantasy city built on a waterfall",
        "A robot playing a guitar on stage",
        "An enchanted garden under the stars",
        "A superhero flying above skyscrapers",
        "A wolf howling at a blood-red moon",
        "A pirate ship sailing through a storm",
        "A child exploring an ancient ruin",
        "A dragon curled around a treasure hoard",
        "A surreal landscape made of candy"
    ]

    for prompt_text in default_prompts:
        obj, created = Suggested_prompt.objects.get_or_create(prompt=prompt_text)
        if created:
            print(f"Created prompt: {prompt_text}")
        else:
            print(f"Prompt already exists: {prompt_text}")
