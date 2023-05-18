import json
import random
import pandas as pd
from config import *


class TeamsFactory:

    def __init__(self, teams_amount, max_programming_languages, max_frameworks, max_platforms, max_databases,
                 max_idioms, max_project_preferences, teams_positions_amount=0, max_cloud_providers=0) -> None:
        self.teams_amount = teams_amount
        self.max_programming_languages = max_programming_languages
        self.max_frameworks = max_frameworks
        self.max_platforms = max_platforms
        self.max_databases = max_databases
        self.max_project_preferences = max_project_preferences
        self.max_idioms = max_idioms
        self.teams_positions_amount = teams_positions_amount
        self.max_cloud_providers = max_cloud_providers

    def create_team_positions(self):
        positions = []
        for i in range(self.teams_positions_amount):
            programming_language_i, frameworks_i, platform_i, idioms_i, project_preferences, databases_i = self._get_random_data_tech()
            cloud_providers_i = self._get_cloud_providers()

            position_i = self._create_position(programming_language_i, frameworks_i, platform_i, databases_i,
                                               cloud_providers_i)
            positions.append(position_i)
        return positions

    def _get_cloud_providers(self):
        n = random.randint(0, self.max_cloud_providers)
        values = []
        cloud_values = get_values(cloud_options)
        for i in range(n):
            j = random.randint(0, len(cloud_options) - 1)
            values.append(cloud_values[j])
        return values

    def _create_position(self, programming_language_i, frameworks_i, platform_i, databases_i, cloud_provider_i):
        return {
            "requirements": {
                "programming_language": programming_language_i,
                "frameworks": frameworks_i,
                "platforms": platform_i,
                "cloud_providers": cloud_provider_i,
                "databases": databases_i,
            }
        }

    def create_teams(self):
        teams = []
        for i in range(self.teams_amount):
            name = f"team_{i}"
            programming_language_i, frameworks_i, platform_i, idioms_i, project_preferences, databases_i = self._get_random_data_tech()
            owner = "9XUXZILjj1NUukUcWQy8FpNQl9F2"
            project_preferences_i = project_preferences
            team_i = self._create_team(name, project_preferences_i, owner, idioms_i, programming_language_i,
                                       frameworks_i, platform_i, databases_i)
            teams.append(team_i)
        return teams

    def _create_team(self, name, project_preferences, owner, idioms, programming_language, frameworks, platforms,
                     databases_i):
        return {
            "name": name,
            "project_preferences": project_preferences,
            "owner": owner,
            "idioms": idioms,
            "technologies": {"programming_language": programming_language, "frameworks": frameworks,
                             "platforms": platforms, "databases": databases_i},
        }

    def create_custom_team(self, name, project_preferences, owner, idioms, programming_language, frameworks, platforms,
                           databases_i):
        return self._create_team(name, project_preferences, owner, idioms, programming_language, frameworks, platforms,
                                 databases_i)

    def _get_random_data_tech(self):
        lengs = []
        fworks = []
        pforms = []
        idioms_i = []
        project_preferences = []
        databases_i = []

        n = random.randint(1, self.max_programming_languages)
        selected = random.randint(1, self.max_programming_languages)
        i = 0
        for j in range(n):
            for leng in frameworks:
                i += 1
                if selected == i:
                    lengs.append(leng)
                    if len(fworks) < self.max_frameworks:
                        fworks.append(frameworks[leng][random.randint(0, len(frameworks[leng]) - 1)]["value"])
                    selected = random.randint(1, self.max_programming_languages)

        n = random.randint(1, self.max_platforms)
        for m in range(n):
            selected = random.randint(0, len(platforms) - 1)
            pforms.append(platforms[selected]["value"])

        n = random.randint(1, self.max_idioms)
        for i in range(n):
            selected = random.randint(0, len(idioms) - 1)
            idioms_i.append(idioms[selected]["value"])

        rand = random.randint(1, self.max_project_preferences)
        for k in range(rand):
            selected = random.randint(0, len(projects_types) - 1)
            project_preferences.append(projects_types[selected])

        rand = random.randint(1, self.max_databases)
        for k in range(rand):
            selected = random.randint(0, len(databases) - 1)
            databases_i.append(databases[selected]["value"])

        lengs = list(set(lengs))
        fworks = list(set(fworks))
        pforms = list(set(pforms))
        idioms_i = list(set(idioms_i))
        project_preferences = list(set(project_preferences))
        databases_i = list(set(databases_i))

        return lengs, fworks, pforms, idioms_i, project_preferences, databases_i

    def get_ideal_team(self, project):
        return {
            "name": "",
            "project_preferences": [project.get("project_type")],
            "owner": "",
            "idioms": project.get("idioms"),
            "technologies": project.get("technologies")
        }


def print_team(team_df, index_team=0):
    print(f"type index: {type(index_team)}")
    print(f"project_type: {team_df.iloc[index_team]['project_preferences']} ")
    print(f"idioms:  {team_df.iloc[index_team]['idioms']}")
    tech = team_df.iloc[index_team]['technologies']
    if type(tech) == str:
        tech = json.loads(tech.replace("\'", "\""))

    print(f"programming_language:  {tech['programming_language']}")
    print(f"frameworks:  {tech['frameworks']}")
    print(f"databases:  {tech['databases']}")
    print(f"platforms:  {tech['platforms']}")


def print_teams_recommendation(teams, recommendations_ids):
    recommendations_ids = [int(x) for x in recommendations_ids]
    i = 1
    for id_i in recommendations_ids:
        print(f"Rank {i}º - Team {id_i}")
        print_team(teams, id_i)
        print("\n")
        i += 1
