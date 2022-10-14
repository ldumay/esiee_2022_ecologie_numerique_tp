# Fichier Models
from app import db
from app.models import Vent

# Entité - Vent
class ControllerVent():

    # All object vent :
    def all ():
        try:
            if len(db.session.query(Vent).all())>0:
                return [ { db.session.query(Vent).all() } ]
            else:
                return "Il n'y a pas de données dans la BDD."
        except:
            return "[Vent-Create] - Error"

    # Create object vent :
    def create (heure, intencite, temperature, vitesse):
        vent_1 = Vent(heure, intencite, temperature, vitesse,
        )
        db.session.add(vent_1)
        db.session.commit()
        #vent_2 = db.session.query(Vent).filter_by(heure=heure, intencite=intencite, temperature=temperature, vitesse=vitesse).get
        #db.session.commit()
        try:
            #return "[Vent-Create] - Vent id="+vent_2.id+" created !"
            return "[Vent-Create] - Vent created !"
        except:
            return "[Vent-Create] - Error"
    
    # Update object vent :
    def update (id, heure, intencite, temperature, vitesse):
        vent = Vent.query.get(id)
        if vent:
            heure = vent.heure if not heure else 0
            intencite = vent.intencite if not intencite else 0
            temperature = vent.temperature if not temperature else 0
            vitesse = vent.vitesse if not vitesse else 0
            db.session.commit()
        try:
            return "[Vent-Update] - Vent id="+id+" updated !"
        except:
            return "[Vent-Update] - Error"

    # Delete object vent :
    def delete (id):
        db.session.query(Vent).filter(Vent.id==id).delete()
        db.session.commit()
        try:
            return "[Vent-Delete] - Vent id="+id+" deleted !"
        except:
            return "[Vent-Delete] - Error"