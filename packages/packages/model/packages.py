from config.extensions import db

class Packages(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(250))
    timer = db.Column(db.Boolean)
    tasks = db.Column(db.Boolean)
    economy = db.Column(db.Boolean)
    

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'timer': self.timer,
            'tasks': self.tasks,
            'economy': self.economy,
        
        }
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_user(cls, userId):
        return cls.query.filter_by(userId=userId).first()
