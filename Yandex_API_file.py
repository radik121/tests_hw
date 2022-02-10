import requests

with open('ya.token.txt', 'r') as file_object:
    token = file_object.read().strip()


class YaAPI:
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }

    def create_folder(self, file_path: str):
        params = {
            "path": file_path,
            "overwrite": "true"
        }
        create = requests.put(self.url, headers=self.headers, params=params)
        print('Папка создана успешно!')
        return create.status_code

    def check_folder(self, folder: str):
        params = {
            "path": folder
        }
        res = requests.get(self.url, headers=self.headers, params=params)
        return res.status_code


if __name__ == '__main__':
    uploader = YaAPI()
    print(uploader.create_folder('netology'))
    print(uploader.check_folder('netology'))