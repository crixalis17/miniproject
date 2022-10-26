import { Component } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatDialog} from "@angular/material/dialog";


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
  onEnter(value: string) { this.value = value; }
  toggle() {
    this.show = !this.show;
  }

}

