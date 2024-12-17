import pytest
import requests

class TestYDCreateFolder:
    def setup_method(self) -> None:
        self.headers = {
            ''
        }

    @pytest.mark.parametrize(
        'param,folder_name,status',
        (
                ('path', 'Image', 201),
                ('path', 'Image', 409),
                ('pathh', 'Music', 400),
        )
    )
    def test_create_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == status