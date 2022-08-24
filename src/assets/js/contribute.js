const technical_search = document.getElementById('technical-search')
const business_search = document.getElementById('business-search')

const technical_table = document.getElementById('technical-table')
const business_table = document.getElementById('business-table')

const funding_card = document.getElementById('funding-card')

const toggle_technical = document.getElementById('toggle-technical')
const toggle_business = document.getElementById('toggle-business')
const toggle_funding = document.getElementById('toggle-funding')

toggle_technical.addEventListener('click', () => {
    technical_search.classList.remove('d-none')
    technical_table.classList.remove('d-none')

    business_search.classList.add('d-none')
    business_table.classList.add('d-none')
    funding_card.classList.add('d-none')
})

toggle_business.addEventListener('click', () => {
    business_search.classList.remove('d-none')
    business_table.classList.remove('d-none')

    technical_search.classList.add('d-none')
    technical_table.classList.add('d-none')
    funding_card.classList.add('d-none')
})

toggle_funding.addEventListener('click', () => {
    funding_card.classList.remove('d-none')

    business_search.classList.add('d-none')
    business_table.classList.add('d-none')
    technical_search.classList.add('d-none')
    technical_table.classList.add('d-none')
})

function FilterTechnicalTable(){
    filter = technical_search.value.toUpperCase()
    trs = technical_table.getElementsByTagName('tr')

    for (i=0; i< trs.length; i++){
        td = trs[i].getElementsByTagName("td")[0];
        if (td){
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                trs[i].style.display = "";
            }
            else{
                trs[i].style.display = "none";
            }
        }
    }
}

function FilterBusinessTable(){
    filter = business_search.value.toUpperCase()
    trs = business_table.getElementsByTagName('tr')

    for (i=0; i< trs.length; i++){
        td = trs[i].getElementsByTagName("td")[0];
        if (td){
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                trs[i].style.display = "";
            }
            else{
                trs[i].style.display = "none";
            }
        }
    }
}