import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})

export class AppComponent {
  title = 'app';
  value = '';
  name1 = 'Ramesh';
    no_of_tweets = 10;
    bullying = 5;
    percentage_bully = 50.00;
  show: boolean=false;
  onEnter(value: string) { this.value = value;


  }
  toggle() {
    this.show = !this.show;
  }
  post() {
console.log(this.value);  }
  public userArray: User[] = [];
  constructor(private http: HttpClient){
    this.http.get('assets/data.csv', {responseType: 'text'})
        .subscribe(
            data => {
              let csvToRowArray = data.split("\n");
              for (let index = 1; index < csvToRowArray.length - 1; index++) {
                let row = csvToRowArray[index].split(",");
                this.userArray.push(new User( row[0],row[1], row[2]));
              }
              console.log(this.userArray[1].value);
            },
            error => {
              console.log(error);
            }
        );
    //this.http.post('url',this.value);
  }

}
export class User{
  id: String;
  attr: String;
  value: String;
  constructor(name: String, bully: String,  percent: String){
    this.id = name;
    this.attr = bully;
    this.value = percent;
  }
}

