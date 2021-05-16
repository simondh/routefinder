# Network Routing sample

## Setup

Using :
* Django 
* djangorestframework
* SQLite



Superuser: name: `route` password: `findaroute`

To set up the SQLite database, simply:

`python manage.py migrate`

as migration `0002_auto_20210516_0957.py` loads the test data

**NOTE** in addition to the test data supplied, I have added a 2-node 
network with no connection to the test network, with nodes 10 and 11.
Thus seeking a route from, say, 1 to 11 should return [], *No Route*

The routes can also be edited using Django ASdmin at `http://127.0.0.1:8000/admin/route_api/routes/`

# testing with Curl:


     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=1&to=4"
    [1, 6, 4]%
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=1&to=2"
    [1, 2]%
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=4&to=1"
    [4, 6, 1]%
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=4&to=11"
    []%
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=4&to=5"
    [4, 5]%
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=1&to=5"
    [1, 6, 4, 5]%
     hewits2 ~ $
     hewits2 ~ $
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=1&to=5a"
    From or To query params are not integers: 1:5a%
     hewits2 ~ $ curl "http://127.0.0.1:8000/r/?from=1"
    Missing From or To query params eg ?from:1&to=2%
     hewits2 ~ $

## Comments

Djangorestframework would have been good. Although overkill for this small
function, it would be useful to have the API documentation.

## Running


## Contact
Simon Hewitt   
simon.d.hewitt@gmail.com   
07799 381001   
