fetch('https://reqres.in/api/users?page=2').then(
    Response => Response.json()
).then(
    responseJSON => createUsersList(responseJSON.data)
).catch(
    err => console.log(err)
); //Presentation from the lecture


function createUsersList(users){
    console.log(users);
  console.log(userToSearch,'daniella');
    const user = users[0];
    console.log(user);
    const curr_main = document.querySelector("main");
    for(let user of users){


             const section = document.createElement('section');
        section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture" />
            <div>
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                    <a href="mailto:${user.email}">Send Email</a>
            </div>
        `;
        curr_main.appendChild(section);


    }
}
