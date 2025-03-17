from config_file import check_json_config, create_json_config
from rw_files import check_file_diff

json_config_filename = "d_manager.json"

if __name__ == "__main__":
    create_json_config(json_config_filename)
    # check_json_config(json_config_filename)
    check_file_diff(json_config_filename)
