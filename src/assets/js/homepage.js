const first_q = document.getElementById('first-question')
const second_q = document.getElementById('second-question')
const answer = document.getElementById('answer')

const bookstore_btn = document.getElementById('bookstore-btn')
const consumer_btn = document.getElementById('consumer-btn')

/*Bookstore cards*/
const card_bookstore = document.createElement('div')
card_bookstore.classList.add('card')
card_bookstore.classList.add('m-4')
const card_body_bookstore = document.createElement('div')
card_body_bookstore.classList.add('card-body')
const card_title_bookstore = document.createElement('h5')
card_title_bookstore.classList.add('card-title')
card_title_bookstore.innerText = 'Έχω βιβλιοπωλείο'
const card_title_bookstore_2 = document.createElement('h5')
card_title_bookstore_2.classList.add('card-title')
card_title_bookstore_2.innerText = 'Σουίτα λογισμικού ERP'
const card_title_bookstore_3 = document.createElement('h5')
card_title_bookstore_3.classList.add('card-title')
card_title_bookstore_3.innerText = 'Αναγνωρισιμότητα'
const card_text_bookstore_2 = document.createElement('p')
card_text_bookstore_2.classList.add('card-text')
card_text_bookstore_2.innerHTML = 'Η εφαρμογή Bookville.gr θα παρέχει πλήρη σουίτα επαγγελματικού λογισμικού διαχείρισης της επιχείρησής σας. Ενδεικτικά, θα προσφέρει διαχείριση εργασιών και ημερομηνιών, διαχείριση πελατολογίου, προβολή χρήσιμων στατιστικών για την εμφάνηση του καταστήματος στις αναζητήσεις των δυνητικών πελατών και πολλά ακόμα. Για μια πλήρη λίστα των παροχών προς τον βιβλιοπώλη, παρακαλώ επισκευθείτε τη σελίδα "Για τον καταστηματάρχη" στην ενότητα "Documentation"'
const card_text_bookstore_3 = document.createElement('p')
card_text_bookstore_3.classList.add('card-text')
card_text_bookstore_3.innerText = 'Η εφαρμογή Bookville.gr θα προσφέρει στα βιβλιοπωλεία τη δυνατότητα να προβάλουν το απόθεμα τους real time στον δυνητικό πελάτη, είτε αυτός αναζητήσει ένα συγκεκριμένο βιβλίο στην περιοχή του, είτε ένα συγκεκριμένο βιβλιοπωλείο. Με αυτή την προβολή, ευελπιστούμε να αυξήσουμε την αναγνωρισιμότητα του βιβλιοπωλείου και να αυξήσουμε την επισκεψιμότητά του. Για μια πλήρη λίστα των παροχών προς τον βιβλιοπώλη, παρακαλώ επισκευθείτε τη σελίδα "Για τον καταστηματάρχη" στην ενότητα "Documentation"'
const card_text_bookstore = document.createElement('p')
card_text_bookstore.classList.add('card-text')
card_text_bookstore.innerText = 'Τι θέλω από την εφαρμογή;'
const usage_btn_1_bookstore = document.createElement('button')
usage_btn_1_bookstore.classList.add('btn')
usage_btn_1_bookstore.classList.add('btn-outline-success')
usage_btn_1_bookstore.classList.add('m-1')
usage_btn_1_bookstore.setAttribute('id','usage-btn-1-bookkstore')
usage_btn_1_bookstore.innerText = 'Σουίτα λογισμικού ERP'
const usage_btn_2_bookstore = document.createElement('button')
usage_btn_2_bookstore.classList.add('btn')
usage_btn_2_bookstore.classList.add('btn-outline-success')
usage_btn_2_bookstore.classList.add('m-1')
usage_btn_2_bookstore.setAttribute('id','usage-btn-2-bookkstore')
usage_btn_2_bookstore.innerText = 'Αναγνωρισιμότητα'

/*Consumer cards*/
const card_consumer = document.createElement('div')
card_consumer.classList.add('card')
card_consumer.classList.add('m-4')
const card_body_consumer = document.createElement('div')
card_body_consumer.classList.add('card-body')
const card_title_consumer = document.createElement('h5')
card_title_consumer.classList.add('card-title')
card_title_consumer.innerText = 'Είμαι καταναλωτής'
const card_title_consumer_2 = document.createElement('h5')
card_title_consumer_2.classList.add('card-title')
card_title_consumer_2.innerText = 'Εξερεύνηση της τοπικής αγοράς'
const card_title_consumer_3 = document.createElement('h5')
card_title_consumer_3.classList.add('card-title')
card_title_consumer_3.innerText = 'Αναζήτηση σε συγκεκριμένο κατάστημα'
const card_text_consumer = document.createElement('p')
card_text_consumer.classList.add('card-text')
card_text_consumer.innerText = 'Τι θέλω από την εφαρμογή;'
const card_text_consumer_2 = document.createElement('p')
card_text_consumer_2.classList.add('card-text')
card_text_consumer_2.innerText = 'Το Bookville.gr παρέχει τη δυνατότητα στον καταναλωτή να ψάξει για όποιο βιβλίο θέλει στα βιβλιοπωλεία της περιοχής του. Η αναζήτηση θα γίνεται πάνω σε ένα διαδραστικό χάρτη. Αφού το βρει, θα έχει τη δυνατότητα να επικοινωνήσει με το βιβλιοπωλείο ή να μεταβεί απευθείας εκεί για να το παραλάβει. Περισσότερα για τις υπηρεσίες προς τους καταναλωτές στη σελίδα "Για τον καταναλωτή" στην ενότητα Documentation'
const card_text_consumer_3 = document.createElement('p')
card_text_consumer_3.classList.add('card-text')
card_text_consumer_3.innerText = 'Τώρα με το Bookville.gr, μπορείς να ψάξεις τον πλήρη κατάλογο διαθεσιμότητας του αγαπημένου σου βιβλιοπωλείου σε πραγματικό χρόνο. Επέλεξε το βιβλιοπωλείο της αρεσκίας σου και βυθίσου στη λίστα των βιβλίων του, πριν αποφασίσεις την επόμενή σου αγορά.  Περισσότερα για τις υπηρεσίες προς τους καταναλωτές στη σελίδα "Για τον καταναλωτή" στην ενότητα Documentation'
const usage_btn_1_consumer = document.createElement('button')
usage_btn_1_consumer.classList.add('btn')
usage_btn_1_consumer.classList.add('btn-outline-danger')
usage_btn_1_consumer.classList.add('m-1')
usage_btn_1_consumer.setAttribute('id','usage-btn-1-consumer')
usage_btn_1_consumer.innerText = 'Εξερεύνηση της τοπικής αγοράς'
const usage_btn_2_consumer = document.createElement('button')
usage_btn_2_consumer.classList.add('btn')
usage_btn_2_consumer.classList.add('btn-outline-danger')
usage_btn_2_consumer.classList.add('m-1')
usage_btn_2_consumer.setAttribute('id','usage-btn-2-consumer')
usage_btn_2_consumer.innerText = 'Αναζήτηση σε συγκεκριμένο κατάστημα'

/*Clear functions*/ 
function Clear_fa() {
    second_q.innerHTML = ''
    answer.innerHTML = ''
}
function Clear_a(){
    answer.innerHTML = ''
}
function Clear_cardbody(){
    card_body_bookstore.innerHTML = ''
    card_body_consumer.innerHTML = ''
}
function Clear_card(){
    card_bookstore.innerHTML = ''
    card_consumer.innerHTML = ''
}
/*Q_1*/

bookstore_btn.addEventListener('click', () => {
    Clear_fa()
    Clear_cardbody()
    Clear_card()
    card_body_bookstore.appendChild(card_title_bookstore)
    card_body_bookstore.appendChild(card_text_bookstore)
    card_body_bookstore.appendChild(usage_btn_1_bookstore)
    card_body_bookstore.appendChild(usage_btn_2_bookstore)
    card_bookstore.appendChild(card_body_bookstore)
    second_q.appendChild(card_bookstore)
})

consumer_btn.addEventListener('click', () => {
    Clear_fa()
    Clear_cardbody()
    Clear_card()
    card_body_consumer.appendChild(card_title_consumer)
    card_body_consumer.appendChild(card_text_consumer)
    card_body_consumer.appendChild(usage_btn_1_consumer)
    card_body_consumer.appendChild(usage_btn_2_consumer)
    card_consumer.appendChild(card_body_consumer)
    second_q.appendChild(card_consumer)
})

/*Q_2*/
usage_btn_1_bookstore.addEventListener('click', () => {
    Clear_fa()
    Clear_cardbody()
    Clear_card()
    card_body_bookstore.appendChild(card_title_bookstore_2)
    card_body_bookstore.appendChild(card_text_bookstore_2)
    card_bookstore.appendChild(card_body_bookstore)
    answer.appendChild(card_bookstore)
})

usage_btn_2_bookstore.addEventListener('click', () => {
    Clear_fa()
    Clear_cardbody()
    Clear_card()
    card_body_bookstore.appendChild(card_title_bookstore_3)
    card_body_bookstore.appendChild(card_text_bookstore_3)
    card_bookstore.appendChild(card_body_bookstore)
    answer.appendChild(card_bookstore)
})

usage_btn_1_consumer.addEventListener('click', () => {
    Clear_fa()
    Clear_cardbody()
    Clear_card()
    card_body_consumer.appendChild(card_title_consumer_2)
    card_body_consumer.appendChild(card_text_consumer_2)
    card_consumer.appendChild(card_body_consumer)
    answer.appendChild(card_consumer)

})

usage_btn_2_consumer.addEventListener('click', () => {
    Clear_fa()
    Clear_cardbody()
    Clear_card()
    card_body_consumer.appendChild(card_title_consumer_3)
    card_body_consumer.appendChild(card_text_consumer_3)
    card_consumer.appendChild(card_body_consumer)
    answer.appendChild(card_consumer)
})