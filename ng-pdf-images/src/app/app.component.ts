import { Component } from '@angular/core';
import { UploadService } from './core/services/upload.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  constructor(private us: UploadService) {}

  fileToUpload = null;

  images = [];

  onSubmit(form) {
    this.us.upload(this.fileToUpload).subscribe((resp: any) => {
      this.images = resp.images;
    });
  }

  handleFileInput(files) {
    console.log(files);
    this.fileToUpload = files.item(0);
  }
}
