window.onload = function() {
    let author_forms = $(`[id^=author_form_]`);
    document.getElementById('id_form-TOTAL_FORMS').value = author_forms.length-2;
}

function updateTypeName(select){
    let text = ['Journal Name', 'Conference Name']
    $('label[for="id_typeName"]').html(text[select.selectedIndex])
}

function addNewAuthor(){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
	$('#author_form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx).replace(/__prefix1__/g, parseInt(form_idx)+1))
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function addExistingAuthor(){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
    let select_element = $('#existing-author-select')[0];
    let select_content = JSON.parse(select_element.value);
	$('#author_form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx).replace(/__prefix1__/g, parseInt(form_idx)+1))
	$(`#id_form-${form_idx}-name`)[0].value = select_content.name;
	$(`#id_form-${form_idx}-surname`)[0].value = select_content.surname;
	$(`#id_form-${form_idx}-email`)[0].value = select_content.email;
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    $('#existing_author_input').val('')
}

function removeAuthor(val){
    let form_idx = $('#id_form-TOTAL_FORMS').val();
    $(`#author_form_${val}`).remove();
    //Update existing forms
    let author_forms = $(`[id^=author_form_]`); //get author forms
    delete author_forms[0] //remove first item (wrapper)
    delete author_forms[author_forms.length-1] //remove last item (empty form)
    console.log(author_forms)
    author_forms = Object.values(author_forms).slice(0,author_forms.length-2); //getting only relevant values
    for(let x = 0; x < author_forms.length; x++){
        author_forms[x].id = `author_form_${x}`;
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/<span>Author \d+/gm,`<span>Author ${x+1}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/data-target="#author_dropdown_\d+/gm,`data-target="#author_dropdown_${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/onclick="toggleAuthorForm\('author_dropdown_icon_\d+/gm,`onclick="toggleAuthorForm('author_dropdown_icon_${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/id="author_dropdown_icon_\d+/gm,`id="author_dropdown_icon_${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/id="author_dropdown_\d+/gm,`id="author_dropdown_${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/removeAuthor\(\d+/gm,`removeAuthor(${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/for="id_form-\d+/gm,`for="id_form-${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/id="id_form-\d+/gm,`id="id_form-${x}`);
        author_forms[x].innerHTML = author_forms[x].innerHTML.replace(/name="form-\d+/gm,`name="form-${x}`);
    }
    $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) - 1);
}

function updateTextValue(textInput){
    textInput.setAttribute('value',textInput.value)
}

function toggleAuthorForm(iconId){
    let icon = document.getElementById(iconId);
    icon.classList.toggle("typcn-arrow-sorted-down");
    icon.classList.toggle("typcn-arrow-sorted-up");
}