1.creer la vm 
python3 -m venv nom
2.nom\Scripts\activate
cela permet de rentrer dans (env)/projet/...
3.(myworld) C:\Users\Your Name>py -m pip install Django
4.pip freeze >requirements.txt
5.django-admin startproject nom_projet
5.lancer le programme à l'aide de 
python3 manage.py runserver(attention à la position)
6.créer la bdd 
python3 manage.py migrate
7.trouver le fichier setting.py, à l'intérrieur vous trouver installed_apps 
ajouter le nom du project