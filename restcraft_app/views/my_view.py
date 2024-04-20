from __future__ import annotations

import typing as t

from restcraft.core import JSONResponse, View

if t.TYPE_CHECKING:
    from restcraft.core import Request


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
