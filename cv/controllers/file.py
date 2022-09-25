from ninja import File,UploadedFile
from ninja import Router
from cv.schema import FileSchema
from typing import List


file_router = Router(tags=['file'])

