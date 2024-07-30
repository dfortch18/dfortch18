import argparse
from abc import ABC, abstractmethod
from enum import Enum
from jinja2 import Environment, FileSystemLoader
from typing import Dict, Any
import json
import yaml


class BadgeProvider(ABC):
    @abstractmethod
    def get_badge(key: str) -> str:
        raise NotImplementedError


class JsonBadgeProvider(BadgeProvider):
    def __init__(self, badge_file_path: str):
        self.badges = self._load_badges(badge_file_path)
        
    def _load_badges(self, badge_file_path: str) -> Dict[str, str]:
        with open(badge_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def get_badge(self, key: str) -> str:
        parts = key.split('.')
        badge = self.badges
        for part in parts:
            badge = badge.get(part, None)
            if badge is None:
                return ''
        return badge


class DataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path: str) -> Dict[str, Any]:
        raise NotImplementedError


class JsonDataLoader(DataLoader):
    def load_data(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)


class YamlDataLoader(DataLoader):
    def load_data(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)


class LoaderType(Enum):
    JSON = 'json'
    YAML = 'yaml'


def get_data_loader(loader_type: LoaderType) -> DataLoader:
    if loader_type == LoaderType.JSON:
        return JsonDataLoader()
    elif loader_type == LoaderType.YAML:
        return YamlDataLoader()


def main():
    parser = argparse.ArgumentParser(description='Update README.md dinamically.')
    parser.add_argument('--data', type=str, required=True, help='Path of the file containing the data.')
    parser.add_argument('--template', type=str, default='templates/README.template.md', help='Path of the README template file.')
    parser.add_argument('--output', type=str, default='README.md', help='Path to the output README file.')
    parser.add_argument('--loader', type=LoaderType, choices=list(LoaderType), default=LoaderType.JSON, help='Custom data loader.')
    
    args = parser.parse_args()
    
    data_loader = get_data_loader(args.loader)
    data = data_loader.load_data(args.data)
    
    badge_provider = JsonBadgeProvider('badges.json')
    
    for tech in data.get('technologies', []):
        badge_key = tech.get('badge')
        if badge_key:
            tech['badge'] = badge_provider.get_badge(badge_key)
    
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(args.template)
    
    readme_content = template.render(data)
    
    with open(args.output, 'w', encoding='utf-8') as output_file:
        output_file.write(readme_content)
    

if __name__ == '__main__':
    main()
