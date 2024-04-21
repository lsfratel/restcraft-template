from __future__ import annotations

import typing as t

from restcraft.core import JSONResponse, View
from restcraft.core.di import inject

if t.TYPE_CHECKING:
    from restcraft.core import Request

    from ..services.example_service import MyExampleService


class MyView(View):
    route = "/"
    methods = ["GET"]

    def handler(self, req: Request) -> JSONResponse:
        return JSONResponse({"hello": "restcraft"})


class MyUUIDView(View):
    route = "/<id:uuid>"
    methods = ["GET"]

    def handler(self, req: Request) -> JSONResponse:
        return JSONResponse(req.params)


class UsersView(View):
    route = "/users"
    methods = ["GET"]

    @inject
    def handler(self, req: Request, user_service: MyExampleService) -> JSONResponse:
        return JSONResponse(user_service.get_users())
