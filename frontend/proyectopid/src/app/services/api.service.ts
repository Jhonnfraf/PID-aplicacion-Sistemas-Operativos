import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface CpuResp {cpu_percent: number;}
export interface MemResp { total: number;
  available: number;
  percent: number;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getCpu(): Observable<CpuResp> {
    return this.http.get<CpuResp>(`${this.apiUrl}/cpu`);
  }

  getMemory(): Observable<MemResp> {
    return this.http.get<MemResp>(`${this.apiUrl}/mem`);
  }
}
