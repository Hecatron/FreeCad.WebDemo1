import { Component, Vue } from 'vue-property-decorator';
import HeaderComponent from './header.vue';
import LeftsidemenuComponent from './leftsidemenu.vue'
import FooterComponent from './footer.vue';

@Component({
    components: {
        HeaderComponent,
        LeftsidemenuComponent,
        FooterComponent
    },
})
export default class DashBoardComponent extends Vue {
}
