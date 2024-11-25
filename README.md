
# Crowdfunding Back End

### Add deployment url
............

![](/resources/beanefactor_test_logo.jpg)
## <strong>Beanefactor</strong> – <em>Where Bean’s Wealth Meets Wag-Worthy Ideas</em>

### Planning:
#### Concept
A crowdfunding-type platform created by a dog (Bean) that that inherits her former owners' multi-million dollar estate, that contains projects created by other dogs that influence how she should spend the money. The purpose of these projects to help other dogs around the world.

#### Intended Audience/User Stories
This platform is targeted at dogs that have ideas on ways Bean can spend her money to help other dogs around the world. They will create a 'project', or concept that other users (or dogs) can support by pledging (or, sacrificing) treats.

### Front End Pages/Functionality
---
TBC
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
---
| HTTP Method | URL              | Purpose              | Request Body   | Success Response Code | Authentication/Authorisation |
|-------------|------------------|----------------------|----------------|-----------------------|------------------------------|
| POST        | /projects/       | Create a new project | Project object | 201                   | Must be logged in            |
| GET         | /projects/       | Retrieve a project   | Project object | 200                   | N/A                          |
| POST        | /pledges/        | Create a new pledge  | Pledge object  | 201                   | Must be logged in            |
| GET         | /pledges/        | Retrieve a pledge    | Pledge object  | 200                   | N/A                          |
| POST        | /api-token-auth/ | Create a new token   | Token object   | 200                   | Must be logged in            |


### DB Schema
![](/resources/beanefactor_ERD_diagram.jpeg)

### Insomnia

