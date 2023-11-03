import random

# List of emojis to use in project names
emojis = [
    "🐍", "🤖", "📊", "🕸️", "🎯", "🖼️", "🎥", "🎮", "💰", "📈", "🎶", "📚", "📝", "💡"
]

# Generate a random Python project name using emojis
def generate_python_project_name_with_emojis():
    # Choose a random number of emojis to use in the project name
    num_emojis = random.randint(1, 5)

    # Choose random emojis from the list
    project_name = "Python PROJECT"
    for i in range(num_emojis):
        emoji = random.choice(emojis)
        project_name += emoji

    return project_name

# Generate a list of Python project name ideas using emojis
def generate_list_of_python_project_name_ideas_with_emojis():
    project_name_ideas = []
    for i in range(10):
        project_name_ideas.append(generate_python_project_name_with_emojis())

    return project_name_ideas

# Print the list of Python project name ideas using emojis
if __name__ == "__main__":
    project_name_ideas = generate_list_of_python_project_name_ideas_with_emojis()

    print("Python project name ideas using emojis:")
    for project_name_idea in project_name_ideas:
        print(project_name_idea)