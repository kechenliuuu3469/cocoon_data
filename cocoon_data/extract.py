import re
import yaml
from collections import OrderedDict

def extract_json_code_safe(s):
    s_stripped = s.strip()
    if (s_stripped.startswith('{') and s_stripped.endswith('}')) or \
       (s_stripped.startswith('[') and s_stripped.endswith(']')):
        return s_stripped

    json_code =  extract_json_code(s_stripped)

    if json_code is not None:
        return json_code

    start_brace = s_stripped.find('{')
    start_bracket = s_stripped.find('[')
    start_index = start_brace if start_bracket == -1 else (start_bracket if start_brace == -1 else min(start_brace, start_bracket))

    if start_index == -1:
        return None

    end_brace = s_stripped.rfind('}')
    end_bracket = s_stripped.rfind(']')
    end_index = end_brace if end_bracket == -1 else (end_bracket if end_brace == -1 else max(end_brace, end_bracket))

    if end_index == -1:
        return None

    potential_json = s_stripped[start_index:end_index + 1]
    return potential_json

def extract_json_code(s):
    import re
    pattern = r"```json(.*?)```"
    match = re.search(pattern, s, re.DOTALL)
    return match.group(1).strip() if match else None

def extract_python_code(s):
    import re
    pattern = r"```python(.*?)```"
    match = re.search(pattern, s, re.DOTALL)
    return match.group(1).strip() if match else None


def extract_yml_code(s):
    import re
    pattern = r"```yml(.*?)```"
    match = re.search(pattern, s, re.DOTALL)
    return match.group(1).strip() if match else None


def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


yaml.add_representer(OrderedDict, represent_ordereddict)




def custom_constructor(loader, node):
    value = loader.construct_scalar(node)
    if value in ['true', 'True', 'TRUE']:
        return True
    elif value in ['false', 'False', 'FALSE']:
        return False
    return str(value)

yaml.SafeLoader.add_constructor('tag:yaml.org,2002:bool', custom_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:str', custom_constructor)



