def recommend_phone_upgrade(
    budget: int,
    preference: str,
    priority: str,
    trade_in: bool,
    condition: str = "good"
) -> dict:
    phones = [
        {"model": "iPhone 15", "os": "iphone", "price": 999, "camera": 9, "battery": 8, "performance": 9, "value": 6},
        {"model": "iPhone 14", "os": "iphone", "price": 899, "camera": 8, "battery": 7, "performance": 8, "value": 7},
        {"model": "iPhone 13", "os": "iphone", "price": 799, "camera": 7, "battery": 8, "performance": 7, "value": 8},
        {"model": "iPhone 12", "os": "iphone", "price": 699, "camera": 6, "battery": 7, "performance": 6, "value": 9},

        {"model": "Pixel 8a", "os": "android", "price": 499, "camera": 9, "battery": 7, "performance": 7, "value": 9},
        {"model": "Pixel 8",  "os": "android", "price": 699, "camera": 9, "battery": 8, "performance": 8, "value": 7},
        {"model": "Galaxy S24","os": "android", "price": 799, "camera": 9, "battery": 8, "performance": 9, "value": 7},
        {"model": "OnePlus 12R","os": "android", "price": 499, "camera": 7, "battery": 9, "performance": 8, "value": 9},
    ]

    preference = preference.strip().lower()
    priority = priority.strip().lower()
    condition = condition.strip().lower()

    
    candidates = [p for p in phones if p["os"] == preference and p["price"] <= budget]

    if not candidates:
        return {
            "error": "No suitable phone found",
            "tip": "Consider increasing your budget or changing your preference."
        }

    # Validate priority
    valid_priorities = ["camera", "battery", "performance", "value"]
    if priority not in valid_priorities:
        return {
            "error": "Invalid priority",
            "tip": "Choose from camera, battery, performance, or value."
        }

    # Sort so the best match is first
    candidates.sort(key=lambda p: p[priority], reverse=True)

    top = candidates[0]
    alternatives = candidates[1:3]  # next 2 options

    monthly_estimate = round(top["price"] / 24)

    notes = []
    if trade_in:
        notes.append("Trade-in selected: promotions may lower monthly cost.")
        if condition in ["cracked", "dead"]:
            notes.append("Device condition may reduce trade-in value.")
    else:
        notes.append("No trade-in selected.")

    return {
        "top_pick": {
            "model": top["model"],
            "price": top["price"],
            "monthly_estimate": monthly_estimate,
            "why": f"Best match for '{priority}' within your ${budget} budget."
        },
        "alternatives": [{"model": a["model"], "price": a["price"]} for a in alternatives],
        "notes": " ".join(notes)
    }
if __name__ == "__main__":
    print(recommend_phone_upgrade(600, "android", "battery", True, "cracked"))
    print(recommend_phone_upgrade(600, "iphone", "camera", False))
