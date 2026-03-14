def recommend_task(emotion):

    if emotion == "Happy":
        return "Creative Work / Brainstorming"

    elif emotion == "Neutral":
        return "Regular Office Tasks"

    elif emotion == "Stressed":
        return "Light Tasks or Break"

    else:
        return "No task recommendation"
