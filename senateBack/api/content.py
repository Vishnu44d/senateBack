from flask import request, Blueprint, jsonify
from senateBack.models.newsModel import News
from base64 import b64encode

contentBP = Blueprint('contentApi', __name__)

@contentBP.route('/news', methods=['GET'])
def get_all_news():
    from server import SQLSession
    session = SQLSession()

    all_news = session.query(News).all()
    session.close()
    if(len(all_news)==0):
        response = {
            "status": "fail",
            "message": "No news yet",
            "payload": []
        }
        return jsonify(response), 201
    else:
        pay = [{
                "title": i.title,
                "content": [j.rstrip() for j in i.content.split("\n")],
                "isFile":i.isFile,
                "file_link": "data:application/pdf;base64,"+str(b64encode(i.supported_doc))[2:-1] if i.isFile else "",
                "date": i.created_on.strftime("%d %m %Y"),
            } for i in all_news]
        response = {
            "status": "success",
            "message": "All news",
            "payload": pay[::-1]
        }
        return jsonify(response), 200

@contentBP.route('/body', methods=['GET'])
def getBody():
    body_type = request.args.get('type', None, type=str)
    from senateBack.models.bodyModel import Body
    from server import SQLSession
    session = SQLSession()

    try:
        all_body = session.query(Body).filter_by(type_of_body=body_type).all()
        session.close()
        response = {
                "status": "success",
                "message": "body",
                "payload": [{
                    "title": i.title,
                    "image": "data:image/jpg;base64, "+str(b64encode(i.image))[2:-1],
                    "name": i.name,
                    "Email": i.email,
                    "Contact": i.contact
                } for i in all_body]
            }
        return jsonify(response), 200
    except:
        response= {
            "status": "fail",
            "message": "internal err",
        }
        return jsonify(response), 502

@contentBP.route('/docs', methods=['GET'])
def getDocs():
    from senateBack.models.documentModel import Document
    from server import SQLSession
    session = SQLSession()

    try:
        all_docs = session.query(Document).all()
        session.close()
        all_titles = [i.type_of_doc for i in all_docs]
        payload = [{"name":i, "data":[]} for i in set(all_titles)]
        for obj in all_docs:
            for i in payload:
                if obj.type_of_doc == i["name"]:
                    i["data"].append({
                        "title":obj.title,
                        "link":"data:application/pdf;base64,"+str(b64encode(i.doc))[2:-1],
                        "date":obj.created_on.strftime("%d %m %Y")
                    })
        # print(payload)
        response = {
                "status": "success",
                "message": "docs",
                "payload": payload
            }
        return jsonify(response), 200
    except Exception as e:
        session.close()
        response= {
            "status": "fail",
            "message": str(e),
        }
        return jsonify(response), 502

@contentBP.route('/slider', methods=['GET'])
def getSlider():
    from senateBack.models.sliderModel import Slider
    from server import SQLSession
    session = SQLSession()

    try:
        all_slides = session.query(Slider).all()
        session.close()
        response = {
                "status": "success",
                "message": "sliders",
                "payload": [
                    {
                        "image":"data:image/jpg;base64, "+str(b64encode(i.image))[2:-1],
                        "title":i.title,
                        "subtitle":i.subtitle
                    } for i in all_slides]
            }
        return jsonify(response), 200
    except Exception as e:
        session.close()
        response= {
            "status": "fail",
            "message": str(e),
        }
        return jsonify(response), 502


@contentBP.route('/socities', methods=['GET'])
def getFest():
    fest = request.args.get('name', None, type=str)
    from senateBack.models.societiesModel import Societies
    from server import SQLSession
    session = SQLSession()

    try:
        all_slides = session.query(Societies).filter_by(society_name=fest).all()
        session.close()
        response = {
                "status": "success",
                "message": "fests",
                "payload": [
                    {
                        "name":i.society_name,
                        "contactname":i.contact_person_name,
                        "phone":i.phone,
                        "email":i.email,
                        "image":"data:image/jpg;base64, "+str(b64encode(i.image))[2:-1],
                        "content":[j.rstrip() for j in i.content.split("\n")]
                    } for i in all_slides]
            }
        return jsonify(response), 200
    except Exception as e:
        session.close()
        response= {
            "status": "fail",
            "message": str(e),
        }
        return jsonify(response), 502