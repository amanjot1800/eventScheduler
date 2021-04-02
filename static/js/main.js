let current_sub_event = 1;

function submitForms() {
    document.getElementById("main").submit();
}

function add_sub_event() {

    let exists = "sub_exists";
    exists += current_sub_event;

    let name = "sub_name";
    name += current_sub_event;

    let date = "sub_date";
    date += current_sub_event;

    let time = "sub_time";
    time += current_sub_event;

    let length = "sub_length";
    length += current_sub_event;

    let location = "sub_location";
    location += current_sub_event;

    let guests = "sub_guests";
    guests += current_sub_event;


    const form = document.getElementById("main");
    const br = document.createElement("br");

    const sub_exists = document.createElement("input");
    sub_exists.setAttribute("type", "hidden");
    sub_exists.setAttribute("name", exists);
    sub_exists.setAttribute("value", "yes");

    const sub_name = document.createElement("input");
    sub_name.setAttribute("type", "text");
    sub_name.setAttribute("name", name);
    sub_name.setAttribute("placeholder", "Event Name");

    const sub_date = document.createElement("input");
    sub_date.setAttribute("type", "date");
    sub_date.setAttribute("name", date);
    sub_date.setAttribute("placeholder", "Date");

    const sub_time = document.createElement("input");
    sub_time.setAttribute("type", "time");
    sub_time.setAttribute("name", time);
    sub_time.setAttribute("placeholder", "Time");

    const sub_length = document.createElement("input");
    sub_length.setAttribute("type", "number");
    sub_length.setAttribute("name", length);
    sub_length.setAttribute("placeholder", "Length");

    const sub_location = document.createElement("input");
    sub_location.setAttribute("type", "text");
    sub_location.setAttribute("name", location);
    sub_location.setAttribute("placeholder", "Location");

    const sub_guests = document.createElement("input");
    sub_guests.setAttribute("type", "text");
    sub_guests.setAttribute("name", guests);
    sub_guests.setAttribute("placeholder", "Guests");

    form.appendChild(sub_exists);
    form.appendChild(br.cloneNode());
    form.appendChild(sub_name);
    form.appendChild(sub_date);
    form.appendChild(sub_time);
    form.appendChild(sub_length);
    form.appendChild(sub_location);
    form.appendChild(sub_guests);

    current_sub_event += 1;

    document.getElementById("subform").appendChild(form);

    if (current_sub_event > 3) {
        document.getElementById("addsub").style.display = "none";
    }
}
