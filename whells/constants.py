ABOUT_DATA = [
    {
        "id": 1,
        "name": "alpha",
        "email": "alpha@gmail.com",
        "role": "supervisor",
        "info": "GCU Faislabad",
    },
    {
        "id": 2,
        "name": "beta",
        "email": "beta@gmail.com",
        "role": "student",
        "info": "GCU Faislabad",
    },
    {
        "id": 3,
        "name": "gamma",
        "email": "gamma@gmail.com",
        "role": "student",
        "info": "GCU Faislabad",
    },
]

ROUTES = {
    "api": [
        {
            "name": "Image Blur",
            "end_point": "http://127.0.0.1:8001/api/v1/whells/cars/card_id/blur-image",
            "params": ["card_id", "same_image_name", "image_path"],
            "description": "from given image path, fetch image then blur and- store at the given location. ",
            "authentication": "No",
        },
        {
            "name": "Car Show",
            "end_point": "http://127.0.0.1:8001/api/v1/whells/cars/card_id",
            "params": ["card_id"],
            "description": "Display the car details of the given car_id.",
            "authentication": "No",
        },
        {
            "name": "Car Create",
            "end_point": "http://127.0.0.1:8001/api/v1/whells/cars/create_car",
            "params": ["All car attributes"],
            "description": "Display the car details of the given car_id.",
            "authentication": "No",
        },
    ],
    "simple": [
        {
            "name": "Home",
            "end_point": "http://127.0.0.1:8001/",
            "params": [],
            "description": "Application homepage",
            "authentication": "No",
        },
        {
            "name": "About",
            "end_point": "http://127.0.0.1:8001/about",
            "params": [],
            "description": "Showing about information.",
            "authentication": "No",
        },
        {
            "name": "Routes",
            "end_point": "http://127.0.0.1:8001/routes",
            "params": [],
            "description": "List of routes in the application.",
            "authentication": "No",
        },
    ],
}
