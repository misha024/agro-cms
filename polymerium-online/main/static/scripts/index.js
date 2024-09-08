document.addEventListener("DOMContentLoaded", () => {
    const allAdditionalContacts = document.querySelectorAll(".section-catalog .additional-contacts")
    const productBlocks = document.querySelectorAll(".section-catalog .product-block")
    const productClickHandler = event => {
        const productBlock = event.target.closest(".product-block")
        const additionalContacts = productBlock.querySelector(".additional-contacts")

        allAdditionalContacts.forEach(contact => {
            contact === additionalContacts && !contact.classList.contains("!flex") ?
                contact.classList.add("!flex") :
                contact.classList.remove("!flex")
        })
    }

    productBlocks.forEach(product => product.addEventListener("click", productClickHandler))
})