# api_dierentuin
## Thema
Ik heb dit thema gekozen omdat ik samen met mijn vriendin graag naar dierentuinen ga. Het is een van onze favoriete uitstapjes om te doen, dus vond ik het een leuk idee om het over een van de dierentuinen te doen waar we dit jaar geweest zijn, Planckendael. Het is een leuke dierentuin die opgedeeld is in werelddelen, wat zorgt voor een leuke ervaring omdat je constant in nieuwe omgevingen komt.

## API
Mijn API is zo gemaakt dat iedereen gegevens kan toevoegen en opvragen. Ik heb daarom voor elke tabel een get- en post-request gemaakt zodat het mogelijk is om managers, regios en dieren toe te voegen en bekijken. Om de reeds toegevoegde gegevens aan te passen of te verwijderen moeten ze eigenaar zijn. Er is slechts 1 persoon die de eigenaar kan zijn. Als er al een eigenaar-account is aangemaakt en iemand wil een nieuw account toevoegen, is dit niet meer mogelijk. Het verwijderen van een eigenaar is ook enkel mogelijk door de eigenaar zelf. Hiervoor heb ik gebruikgemaakt van Oauth2. Voor het aanpassen van de gegevens heb ik gebruikgemaakt van een put-request.
Ik heb ook een front-end gemaakt, dat gebruikt kan worden als informatie pagina van de dierentuin. Het geeft een overzichtelijk beeld en mensen kunnen er zowel gegevens op aanvragen als toevoegen. 

[Netlify front-end](https://main--fancy-faun-0a0ecd.netlify.app/)

### [Link API](https://api-dierentuin-michielkuyken.cloud.okteto.net/)

## Postman requests screenshots
Post eigenaar:

![post eigenaar screenshot](/screenshots/post_eigenaar.png)

Delete eigenaar:

![delete eigenaar screenshot](/screenshots/delete_eigenaar.png)

Eigenaar authorization:

![eigenaar authorization screenshot](/screenshots/authorization.png)

Post manager:

![post manager screenshot](/screenshots/post_manager.png)

Get managers:

![get managers screenshot](/screenshots/get_managers.png)

Get manager by manager nummer:

![get manager by_managernummer_screenshot](/screenshots/get_manager_by_managernummer.png)

Put manager:

![put manager screenshot](/screenshots/put_manager.png)

Delete manager:

![delete manager screenshot](/screenshots/delete_manager.png)

Post regio:

![post regio screenshot](/screenshots/post_regio.png)

Get regios:

![get regios screenshot](/screenshots/get_regios.png)

Get regio by regionaam:

![get regio_by_regionaam screenshot](/screenshots/get_regio_by_regionaam.png)

Put regio:

![put regio screenshot](/screenshots/put_regio.png)

Delete regio:

![delete regio screenshot](/screenshots/delete_regio.png)

Post dier:

![post dier screenshot](/screenshots/post_dier.png)

Get dieren:

![get dieren screenshot](/screenshots/get_dieren.png)

Get dier by diersoort:

![get dier_by_diersoort screenshot](/screenshots/get_dier_by_diersoort.png)

Get dier by regio:

![get dier_by_regio screenshot](/screenshots/get_dier_by_regio.png)

Put regio:

![put regio screenshot](/screenshots/put_regio.png)

Delete regio:

![delete regio screenshot](/screenshots/delete_regio.png)

## OpenAPI docs screenshots
Docs screenshot:

![docs screenshot](/screenshots/docs_screenshot.png)
