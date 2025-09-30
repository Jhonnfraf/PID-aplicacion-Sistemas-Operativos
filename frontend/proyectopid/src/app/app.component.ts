import { Component, OnInit } from '@angular/core';
/*import { RouterOutlet } from '@angular/router';*/
import { ApiService, CpuResp, MemResp } from './services/api.service';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  imports: [CommonModule /*, RouterOutlet*/],
  standalone: true
})


export class AppComponent implements OnInit {
  cpu: number | null = null;
  memory: MemResp | null = null;

  constructor(private api: ApiService) {}

  ngOnInit(){
      this.api.getCpu().subscribe((res : CpuResp) => {
        this.cpu = res.cpu_percent;
      });
      this.api.getMemory().subscribe((res : MemResp) => {
        this.memory = res;
      });
  }
}
