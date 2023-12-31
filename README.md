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

![post eigenaar screenshot](/Screenshots/post_eigenaar.png)

Delete eigenaar:

![delete eigenaar screenshot](/Screenshots/delete_eigenaar.png)

Eigenaar authorization:

![eigenaar authorization screenshot](/Screenshots/authorization.png)

Post manager:

![post manager screenshot](/Screenshots/post_manager.png)

Get managers:

![get managers screenshot](/Screenshots/get_managers.png)

Get manager by manager nummer:

![get manager by_managernummer_screenshot](/Screenshots/get_manager_by_managernummer.png)

Put manager:

![put manager screenshot](/Screenshots/put_manager.png)

Delete manager:

![delete manager screenshot](/Screenshots/delete_manager.png)

Post regio:

![post regio screenshot](/Screenshots/post_regio.png)

Get regios:

![get regios screenshot](/Screenshots/get_regios.png)

Get regio by regionaam:

![get regio_by_regionaam screenshot](/Screenshots/get_regio_by_regionaam.png)

Put regio:

![put regio screenshot](/Screenshots/put_regio.png)

Delete regio:

![delete regio screenshot](/Screenshots/delete_regio.png)

Post dier:

![post dier screenshot](/Screenshots/post_dier.png)

Get dieren:

![get dieren screenshot](/Screenshots/get_dieren.png)

Get dier by diersoort:

![get dier_by_diersoort screenshot](/Screenshots/get_dier_by_diersoort.png)

Get dier by regio:

![get dier_by_regio screenshot](/Screenshots/get_dier_by_regio.png)

Put regio:

![put regio screenshot](/Screenshots/put_regio.png)

Delete regio:

![delete regio screenshot](/Screenshots/delete_regio.png)

## OpenAPI docs screenshots
Docs screenshot:

![docs screenshot](/Screenshots/docs_screenshot.png)
