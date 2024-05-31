
from .module import clean_data_base
import random
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from faker import Faker
from api.models import Person, CustomUser, Agent, Driver, Criteria, Almond, ControlPoint, ControlPointByAgent, RoadControl, CriteriaByControl, Vehicle

fake = Faker()

def run():
    print("::::::::::::::::::::: clean database :::::::::::::::::::::")
    clean_data_base()
    return
    print("::::::::::::::::::::: Create seed :::::::::::::::::::::")
    create_users(5)
    create_agents(5)
    create_drivers(5)
    create_criteria(10)
    create_almonds(20)
    create_control_points(15)
    create_control_point_by_agents(50)
    create_road_controls(100)
    create_criteria_by_controls(200)
    create_vehicles(25)



def create_users(num_users):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        sexe = random.choice(['F', 'M'])
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            sexe=sexe,
            date_of_birth=date_of_birth
        )

def create_agents(num_agents):
    for _ in range(num_agents):
        person = Person.objects.order_by('?').first()
        matricule = fake.unique.random_number(digits=8)
        Agent.objects.create(
            first_name=person.first_name,
            last_name=person.last_name,
            email=person.email,
            phone_number=person.phone_number,
            sexe=person.sexe,
            date_of_birth=person.date_of_birth,
            matricule=matricule,
            user=User.objects.create_user(username=person.phone_number, password="123456789")
        )

def create_drivers(num_drivers):
    for _ in range(num_drivers):
        person = Person.objects.order_by('?').first()
        license_number = fake.unique.random_number(digits=8)
        Driver.objects.create(
            first_name=person.first_name,
            last_name=person.last_name,
            email=person.email,
            phone_number=person.phone_number,
            sexe=person.sexe,
            date_of_birth=person.date_of_birth,
            license_number=license_number
        )

def create_criteria(num_criteria):
    for _ in range(num_criteria):
        name = fake.unique.word()
        description = fake.sentence()
        Criteria.objects.create(
            name=name,
            description=description
        )

def create_almonds(num_almonds):
    for _ in range(num_almonds):
        montant = fake.random_int(min=50, max=500)
        paid = fake.boolean()
        Almond.objects.create(
            montant=montant,
            paid=paid
        )

def create_control_points(num_control_points):
    for _ in range(num_control_points):
        name = fake.unique.word()
        gps_location = fake.unique.word()
        ControlPoint.objects.create(
            name=name,
            gps_location=gps_location
        )

def create_control_point_by_agents(num_relations):
    agents = Agent.objects.all()
    control_points = ControlPoint.objects.all()
    for _ in range(num_relations):
        agent = random.choice(agents)
        control_point = random.choice(control_points)
        state = random.choice(['Active', 'Inactive'])
        ControlPointByAgent.objects.create(
            agent=agent,
            control_point=control_point,
            state=state
        )

def create_road_controls(num_controls):
    agents = Agent.objects.all()
    control_points = ControlPoint.objects.all()
    for _ in range(num_controls):
        date = fake.date_between(start_date='-1y', end_date='today')
        control_point = random.choice(control_points)
        agent = random.choice(agents)
        RoadControl.objects.create(
            date=date,
            control_point=control_point,
            agent=agent
        )

def create_criteria_by_controls(num_relations):
    criteria = Criteria.objects.all()
    road_controls = RoadControl.objects.all()
    almonds = Almond.objects.all()
    for _ in range(num_relations):
        criterion = random.choice(criteria)
        road_control = random.choice(road_controls)
        state = random.choice(['Passed', 'Failed'])
        almond = random.choice(almonds)
        CriteriaByControl.objects.create(
            criteria=criterion,
            road_control=road_control,
            state=state,
            almond=almond
        )

def create_vehicles(num_vehicles):
    for _ in range(num_vehicles):
        immatriculation = fake.unique.random_number(digits=8)
        Vehicle.objects.create(
            immatriculation=immatriculation
        )





