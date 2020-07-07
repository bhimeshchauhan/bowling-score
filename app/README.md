Bowling
======================================


                             ! ! ! !
                          ." ! ! !  /
                        ."   ! !   /
                      ."     !    /
                    ."           /
                  ."     o      /
                ."             /
              ."              /
            ."               /
          ."      . '.      /
        ."      '     '    /
      ."                  /
    ."     0 |           /
           |/
          /|
          / |

### Instructions to run the all

#### Client - @access [http://localhost:3000/]

##### Run
- run `cd app/client`
- run `npm run`
##### Test
- run `cd app/client`
- run `npm test`

#### Server - @access [http://localhost:8000/]

##### Admin - @access [http://localhost:8000/admin/]
- @email: `admin@admin.com`
- @username: `admin`
- @password: `adminpassword`
##### Run
- run `cd app/server`
- run `source env/bin/activate`
- run `pip install -r requirements.txt`
- run `python manage.py runserver`
##### Test
- run `cd app/server`
- run `django test`