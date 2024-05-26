# ROUTES

Following API's routes are available in this application.


## Car
#### Car Registration
* Post
  * http://localhost:8000/api/v1/whells/cars/create
    * Params: all car attributs
      * Example: http://localhost:8000/api/v1/whells/cars/1/create
-#### Image Blur
* Post
  * http://localhost:8000/api/v1/whells/cars/card_id/blur-image
    * Params: image_path
      * Example: http://localhost:8000/api/v1/whells/cars/1/blur-image
#### Car Infor Show
* Get
  * http://localhost:8000/api/v1/whells/cars/card_id
    * Example: http://localhost:8000/api/v1/whells/cars/1
