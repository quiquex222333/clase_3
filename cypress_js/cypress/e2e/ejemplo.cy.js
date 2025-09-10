
describe("Mi primer test case en cypress", () => {
    it('Prueba visita la pagina de ejemplo para validar el titulo', () => {
        cy.visit('https://example.cypress.io')
        cy.contains('Kitchen Sink')
        cy.get('h1').should('contain', 'Kitchen Sink')
    })
})