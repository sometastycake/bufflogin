from pydantic import BaseModel


class BuffAuthorizationStatus(BaseModel):
    code: str
    error: str

    def is_authorized(self) -> bool:
        return 'Login Required' not in self.code
