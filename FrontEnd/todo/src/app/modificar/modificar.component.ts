import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import { Todo,TaskItem } from '../api.service';

@Component({
  selector: 'app-modificar',
  templateUrl: './modificar.component.html',
  styleUrls: ['./modificar.component.css']
})
export class ModificarComponent {

  todo: Todo = {
    id:'',
    name: '',
    date: new Date(),
    desc: '',
    task: []
  };
  taskInput: string = '';

  constructor(private apiService: ApiService) { }

  onSubmit() {
    this.apiService.savetodo(this.todo).subscribe(
      response => {
        console.log('Todo guardado correctamente:', response);
      },
      error => {
        console.error('Error al guardar el todo:', error);
      }
    );
  }

}
