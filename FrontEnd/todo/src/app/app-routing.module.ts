import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main/main.component';
import { TodosComponent } from './todos/todos.component';
import { ModificarComponent } from './modificar/modificar.component';

const routes: Routes = [
  {path:'main',component:MainComponent},
  {path:'todos',component:TodosComponent},
  {path:'modificar',component:ModificarComponent}];
  

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
