Feature: Pruebas de API para la aplicación client.py

Background:
  * url 'http://localhost:3000'

Scenario: Prueba del endpoint /igv
  Given path '/igv'
  When method GET
  Then status 200
  And match response.igv == 15
Scenario: Prueba de respuesta erronea con otro valor de IGV
    Given path '/igv'
    When method GET
    Then status 200
    And match response.igv == 20
  

  
  

