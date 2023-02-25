
from flask import Blueprint

bp = Blueprint(
    name="basic",
    import_name=__name__,
)

@bp.route("/members", methods=["GET", "POST"])
def members():
    return {"members": ["member1", "member2", "member3"]}