import argparse
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
import json


def load_data(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_template(data: Dict[str, Any], output_file: str):
    template_path = 'templates/' + data['template'] + '.md'
    
    template_data = data['data']
    
    badges_data = load_data('badges.json')
    
    template_data['badges_url'] = badges_data['url']
    template_data['badges'] = badges_data['badges']
    
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    
    readme_content = template.render(template_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    

def main():
    parser = argparse.ArgumentParser(description='Generate Github Profile\'s README.md')
    parser.add_argument('--data', type=str, required=True, help='Path of the file containing the data.')
    parser.add_argument('--output', type=str, default='README.md', help='Path of the output README.md file.')
    
    args = parser.parse_args()
    
    data = load_data(args.data)
    
    generate_template(data, args.output)

if __name__ == '__main__':
    main()
