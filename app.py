from PySide2 import QtWidgets,QtCore
from movie import get_movies
from movie import Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.setup_ui()
        self.setup_connections()
        self.populate()
        

    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.placehoder = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Ajouter un Film")
        self.text = QtWidgets.QListWidget()
        self.text.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete = QtWidgets.QPushButton("Supprimer un Film")
        


        self.layout.addWidget(self.placehoder)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.btn_delete)
       
    def setup_connections(self):
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_delete.clicked.connect(self.remove_movie)
        self.placehoder.returnPressed.connect(self.add_movie)
    
    def populate(self): 
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole,movie)
            self.text.addItem(lw_item)


    def add_movie(self):
        movie_title = self.placehoder.text()
        if not movie_title:
            return False

        movie = Movie(title=movie_title)
        resultat = movie.add_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole,movie)
            self.text.addItem(lw_item)
            self.placehoder.setText("")


    
    def remove_movie(self):
        for selected_item in self.text.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movie()
            self.text.takeItem(self.text.row(selected_item))






app = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()