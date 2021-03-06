import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class UploadService {
  constructor(private http: HttpClient) {}

  upload(data) {
    return this.http.post(`${environment.apiEndpoint}/api/pdf/`, data);
  }
}
