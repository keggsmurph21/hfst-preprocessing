import yaml
import argparse

def parse_yaml(fp):

    return yaml.load(fp)

def gen_lexc(yaml_data):

    lexc_data = yaml_data

    return lexc_data

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('yaml_file', type=argparse.FileType('r'))
    args = parser.parse_args()

    yaml_data = parse_yaml(args.yaml_file)
    lexc_data = gen_lexc(yaml_data)

    print(lexc_data)
