# FishHunt-Backend
The python backend part of stationed kid's game made for Primorsky Aquarium. Writen in *tensorflow* and *django rest framework*

## Modules
Prodject consists of
- Classificator (Neural model)
- Django REST Backend

## Deploing
1. install requirmented librarys
    > pip install -r requirments.txt
2. Upload a dataset for training. It must have a following structure (there may be any fish folders ofc):
    Dataset/
    ├─ Fish_Dataset/
    │  ├─ Fish1/
    │  │  ├─ *.jpg
    │  ├─ Fish2/
    │  │  ├─ *.jpg
3. Run a *create_model.ipynb* notebook to create your's neural model
    > jupyter-lab
4. Run a server
    > cd Fishhunt && python manage.py runserver

## Usage
1. Create user for django admin panel
    > python manage.py createsuperuser
2. Got to *localhost:8000/admin* to create fish models
3. Get model_label parameters from *labels* var in notebook

## License
This code is totally free to use and modify if you have concrete author

## Author
- Telegram: @BeaverNotACat
- Discord: Бобр#0977
- IRL: Vanya

## Thanks to
- All personel Department of pre-university education
- My *frontend teammates*
- Andrey and Matvey: you are weak teachers but greate mates <3
