import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


export interface TaskItem {
  idtask?: string
  description: string
  completed: boolean
  date: Date
}

export interface Todo {
  id?: string; 
  name: string;
  desc: string;
  date: Date;
  task: TaskItem[];
}


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';


  constructor(private http: HttpClient) { }

  getTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(`${this.apiUrl}/todo`);
  }

  public savetodo(model: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/todo`, model)
  } 

  
}
