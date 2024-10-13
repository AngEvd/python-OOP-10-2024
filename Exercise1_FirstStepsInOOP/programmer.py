class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int):
        if skills_needed <= self.skills:
            if new_language != self.language:
                message = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
                return message
            else:
                return f"{self.name} already knows {new_language}"
        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills"
