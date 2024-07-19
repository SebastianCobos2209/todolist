import { Component, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'todo';

  showSection: boolean = true;
todos: any;

  constructor(private router: Router) {}

  ngOnInit(): void {
    
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.showSection = this.router.url === '/'; // Ocultar sección si la ruta no es '/'
      }
    });
  }
  
}

  