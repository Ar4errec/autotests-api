from httpx import Client, URL, QueryParams, Response
from typing import Any

# Типы для совместимости с httpx
RequestData = dict[str, Any] | list[tuple[str, Any]] | None
RequestFiles = dict[str, Any] | list[tuple[str, Any]] | None

class APIClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData = None,
        files: RequestFiles = None
    ) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)
