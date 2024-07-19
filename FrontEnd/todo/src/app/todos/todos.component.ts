import { Component } from '@angular/core';
import { ApiService, Todo } from '../api.service';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})
export class TodosComponent {
  todos: Todo[] = [];

  displayedColumns: string[] = ['position', 'name','desc', 'date', 'tasks']; // Definir las columnas que usarás

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.loadTodos();
  }

  loadTodos(): void {
    this.apiService.getTodos().subscribe(data => {
      this.todos = data;
    });
  }

  
}
